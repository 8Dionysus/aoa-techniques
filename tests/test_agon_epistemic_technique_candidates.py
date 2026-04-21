from __future__ import annotations
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_generated_registry_shape():
    reg = json.loads((ROOT / 'generated/agon_epistemic_technique_candidates.min.json').read_text(encoding='utf-8'))
    assert reg['wave'] == 'XV'
    assert reg['runtime_posture'] in ('candidate_only', 'pre_protocol_candidate_only')
    assert reg['count'] == 10
    assert len(reg['techniques']) == 10
    for item in reg['techniques']:
        assert item['live_protocol'] is False
        assert 'auto_doctrine_rewrite' in item.get('forbidden_effects', [])

def test_builder_check_and_validator():
    assert subprocess.run([sys.executable, str(ROOT / 'scripts/build_agon_epistemic_technique_candidates.py'), '--check'], cwd=ROOT).returncode == 0
    assert subprocess.run([sys.executable, str(ROOT / 'scripts/validate_agon_epistemic_technique_candidates.py')], cwd=ROOT).returncode == 0
