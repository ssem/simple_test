import mock
import socket
import unittest
from requests_test.example import Example


### example of a simple test ###
class Test_Init(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        ### import our class we want to test ###
        cut = Example()
        ### make some assertions ###
        self.assertTrue(hasattr(cut, 'test'))
        self.assertTrue(cut.test == 'test assignment')

### example of a test where we get the expected response ###
class Test_Get_Headers(unittest.TestCase):
    def setUp(self):
        self.cut = Example()

    def tearDown(self):
        pass

    ### this patches requests with a mock object ###
    ### the real requests will never be called and we will never connect to google.com ###
    @mock.patch('requests_test.example.requests')
    def test_get_headers(self, mock_requests):
        ### this addeds the get function to our mock_requests ###
        ### we need this because we call request.get() in our code ###
        mock_requests.get = mock.Mock()

        ### call our real function so shit can happen ###
        response = self.cut.get_headers()
        ### shit happened now lets assert that our fake requests.get() function was called ###
        mock_requests.get.assert_called_with(
            url='http://www.google.com',
            timeout=5)
        ### and assert that we got the response we were looking for ###
        self.assertEqual(response, mock_requests.get.return_value.headers)

    ### once again patch requests so the real library is never called ###
    @mock.patch('requests_test.example.requests')
    def test_get_headers_timeout(self, mock_requests):
        ### add get() function to our fake requests ###
        mock_requests.get = mock.Mock()
        ### this time we tell get() to raise socket.timeout when it is called ###
        mock_requests.get.side_effect = socket.timeout # <<< this is the foo you are looking for

        ### assert that socket.timeout was never caught ###
        with self.assertRaises(socket.timeout):
            self.cut.get_headers()
        ### and we can still check the parameters passed to mock.get ###
        mock_requests.get.assert_called_with(
            url='http://www.google.com',
            timeout=5)
