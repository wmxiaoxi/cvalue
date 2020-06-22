import pytest
import allure
def test_main():
    # pytest.main(['-v', '-s', 'test_cases/', '--html=report/report.html', '--self-contained-html'])
     pytest.main(['-q', '-s', 'cases/', '--alluredir', './result','--reruns','3','--reruns-delay','3'])     #allure serve result
if __name__=="__main__":
    test_main()