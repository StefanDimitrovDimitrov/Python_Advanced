import unittest
from unittest import mock
from testing import callAPI


class callApiTest(unittest.TestCase):
    def test_get_my_daily_tasks(self):
        mock_value = {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}
        with unittest.mock.patch('callAPI.get_task', return_value = mock_value):
            daily_tasks = callAPI.my_daily_todo()
        # self.assertEqual(daily_tasks, [{
        #     "userId": 1,
        #     "id": 1,
        #     "title": "delectus aut autem",
        #     "completed": False
        # }])

if __name__ == '__main__':
    unittest.main()