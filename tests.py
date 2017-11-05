import charts
import unittest
import io
import csv
from charts import analyze_data_data


class AppTestCase(unittest.TestCase):
    def setUp(self):
        charts.app.testing = True
        charts.app.config['DEBUG'] = True
        self.app = charts.app.test_client()
        self.assertEqual(charts.app.debug, True)

    def tearDown(self):
        pass

    def test_root_page(self):
        response = self.app.get('/', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_error_404(self):
        response = self.app.get('/cohort5', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_cohort1_page(self):
        response = self.app.get('/cohort1', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def data_import(self):
        output = io.BytesIO()
        writer = csv.writer(output)
        writer.writerow("3121,2016-07-19,40,0,0")
        writer.writerow("3122,2016-07-19,40,0,0")
        data = format_data(output.getvalue())
        self.assertEqual(data, [100, 100, 100, 0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
