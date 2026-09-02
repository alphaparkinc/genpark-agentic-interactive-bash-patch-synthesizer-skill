from client import AgenticInteractiveBashPatchSynthesizerClient

def main():
    client = AgenticInteractiveBashPatchSynthesizerClient()
    res = client.synthesize_git_diff_patch('Resolve race condition in connection pool acquire()')
    print('Interactive Bash Patch Synthesizer: ' + res['patch_session_id'])
    print('Actions: ' + str(res['interactive_actions_taken_count']) + ' | Test Passed: ' + str(res['reproduced_unit_test_passed']))
    print('Modified Files: ' + ', '.join(res['modified_files']))
    print('Patch Artifact: ' + res['patch_artifact_url'])

if __name__ == '__main__':
    main()
