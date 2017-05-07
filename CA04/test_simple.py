
import unittest

from simple_copy import get_commits, read_file, get_dates, get_authors, get_week_days

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')
        self.commits = get_commits(self.data)
        self.dates = get_dates(self.commits)
        self.authors = get_authors(self.commits)
        self.week_day = get_week_days(self.commits)

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        
    def test_first_dates(self):
        dates_test = get_dates(self.commits)
        self.assertEqual('2015-07-13 09:21:48 +0100 (Mon, 13 Jul 2015)',self.dates[0])
        
    def test_first_name(self):
        name_test = get_authors(self.commits)
        self.assertEqual('Thomas',self.authors[0])
    
    def test_week_day(self):
        week_day_test = get_week_days(self.commits)
        self.assertEqual('Fri',self.week_day[0])

if __name__ == '__main__':
    unittest.main()
