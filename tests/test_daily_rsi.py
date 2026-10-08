import copy
import importlib.util
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('daily_rsi',ROOT/'scripts/daily_rsi.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class CurationTests(unittest.TestCase):
    def setUp(self):
        self.zh=(ROOT/'README.md').read_text(encoding='utf-8')
        self.en=(ROOT/'README.en.md').read_text(encoding='utf-8')
        self.evidence={'repository':'test-owner/fixture-agent','sha':'a'*40,
            'sources':{'update.py':{'excerpt':'1: skill.write_text(candidate)\n2: return result','line_count':2}}}
        self.entry={'qualified':True,'name':'FixtureAgent','category':'skills',
            'citations':[{'path':'update.py','line':1,'quote':'write_text(candidate)'}],
            'zh':{'object':'技能文本','weights':'未训练权重','finding':'把候选写入技能文件','value':'复用技能更新路径','limitations':'仅静态核查；未复现实验'},
            'en':{'object':'Skill text','weights':'No weight training','finding':'Writes candidates into skill files','value':'Reusable skill-update path','limitations':'Static inspection only; experiments not reproduced'}}

    def test_one_addition_preserves_existing_methods_and_urls(self):
        self.assertTrue(m.validate_entry(self.entry,self.evidence,self.zh))
        zh=m.render_entry(self.zh,self.entry,self.evidence,'zh','2026-10-08')
        en=m.render_entry(self.en,self.entry,self.evidence,'en','2026-10-08')
        count=len(re.findall(r'^#### ',self.zh,re.M))
        m.validate_pair(zh,en,count)
        for old in re.findall(r'^#### .+$',self.zh,re.M):
            self.assertIn(old,zh)
        for old in re.findall(r'\]\((https?://[^)]+)\)',self.zh):
            self.assertIn(old,zh)
        self.assertIn(f'**{count+1} 个方法条目',zh)
        self.assertIn('#L1)',zh)

    def test_invalid_source_quote_rejected(self):
        self.entry['citations'][0]['quote']='never observed'
        with self.assertRaises(ValueError): m.validate_entry(self.entry,self.evidence,self.zh)

    def test_valid_quote_at_wrong_line_rejected(self):
        self.entry['citations'][0]['line']=2
        with self.assertRaises(ValueError): m.validate_entry(self.entry,self.evidence,self.zh)

    def test_markup_injection_rejected(self):
        self.entry['zh']['finding']='text\n| injected row |'
        with self.assertRaises(ValueError): m.validate_entry(self.entry,self.evidence,self.zh)

    def test_repository_alias_duplicate_rejected(self):
        self.evidence['repository']='MineDojo/Voyager'
        with self.assertRaises(ValueError): m.validate_entry(self.entry,self.evidence,self.zh)

    def test_unknown_category_rejected(self):
        self.entry['category']='SEO'
        with self.assertRaises(ValueError): m.validate_entry(self.entry,self.evidence,self.zh)

    def test_daily_limit_survives_retries(self):
        state={'additions':[{'date':'2026-10-08','name':'FixtureAgent'}]}
        self.assertTrue(m.already_added(state,'2026-10-08'))
        self.assertFalse(m.already_added(state,'2026-10-09'))

    def test_missing_anchor_stops_edit(self):
        broken=self.zh.replace('<a id="skills"></a>','')
        with self.assertRaises(ValueError): m.render_entry(broken,self.entry,self.evidence,'zh','2026-10-08')

    def test_translation_mismatch_rejected(self):
        zh=m.render_entry(self.zh,self.entry,self.evidence,'zh','2026-10-08')
        en=m.render_entry(self.en,self.entry,self.evidence,'en','2026-10-08').replace('#### FixtureAgent','#### OtherAgent')
        with self.assertRaises(ValueError): m.validate_pair(zh,en,len(re.findall(r'^#### ',self.zh,re.M)))


if __name__=='__main__': unittest.main()
