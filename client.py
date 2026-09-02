class AgenticInteractiveBashPatchSynthesizerClient:
    def synthesize_git_diff_patch(self, issue_description='Fix IndexError in tokenizer offset mapping when padding=False', repo_directory_context='/app/transformers'):
        return {
            'patch_session_id': 'swe_ptc_8812',
            'interactive_actions_taken_count': 7,
            'modified_files': ['src/transformers/tokenization_utils_base.py'],
            'unified_diff_patch_text': '--- a/tokenization.py\n+++ b/tokenization.py\n@@ -104,2 +104,4 @@\n+ if not offsets:\n+     return []',
            'reproduced_unit_test_passed': True,
            'patch_artifact_url': 'https://swe.genpark.ai/patches/8812.patch'
        }
