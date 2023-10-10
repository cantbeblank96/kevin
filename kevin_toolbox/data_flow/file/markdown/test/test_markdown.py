import pytest
from kevin_toolbox.patches.for_test import check_consistency
from kevin_toolbox.data_flow.file import markdown
from test_data.for_generate_table.data_s import content_s_ls, param_s_ls, expected_result_ls


@pytest.mark.parametrize("content_s, param_s, expected_result",
                         zip(content_s_ls, param_s_ls, expected_result_ls))
def test_reader(content_s, param_s, expected_result):
    print("test markdown.generate_table")

    check_consistency(markdown.generate_table(content_s=content_s, **param_s).strip(), expected_result.strip())
