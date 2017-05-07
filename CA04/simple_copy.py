import pandas as pd

def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
                        # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(), 
                'week_day': details[2].strip().split(' ')[3][1:4],
                'number_of_lines': details[3].strip().split(' ')[1],
                'line count': int(details[3].strip().split(' ')[0])
            }
            
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

def get_dates(commits):
    dates = []
    index = 0
    count = 0
    while index < len(commits):
        date = (commits[index]['date'])
        index = index + 1
        #create list of dates for analysis
        if date not in dates:
                dates.append(date)
                dates.sort()
    
    return dates 
    
def get_authors(commits):
    authors = []
    index = 0
    count = 0
        
    while index < len(commits):
        author = (commits[index]['author'])
        index = index + 1
        #create list of unique authors for analysis
        if author not in authors:        
            authors.append(author)
         
    return authors
    

def get_week_days(commits):
    week_days = []
    index = 0
    count = 0
    
    while index < len(commits):
        week_day = (commits[index]['week_day'])
        index = index + 1
        #create list of week days
        week_days.append(week_day)
        week_days.sort()
        
    return week_days
    
def get_names(get_authors):
    index = 0
    count = 0
    name=raw_input('Enter name:')
    
    while index < len(commits):
        author = (commits[index]['author'])
        index = index + 1
        if author == name:
            count = count + 1
    
    per_cent = round((float(count) / len(commits)) * 100,2)
    print '{} made {} commits, which is {}% of total commits'.format(name,count,per_cent)
    
                
if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    date_analysis = get_dates(commits)
    author_analysis = get_authors(commits)
    day_analysis = get_week_days(commits)
        
    # print the number of lines read
    print(len(data))
    #print(commits)
    print(commits[0])
    print(commits[1]['author'])
    print(len(commits))
    
    #analysis of dates
    print(date_analysis[0])
    print(date_analysis[-1])
    
    #analysis of names
    print(author_analysis[0])
    #analysis of authors - enter name to find % of total commits for that person
    name_check = get_names(get_authors)
    
    #analysis of days
    print(day_analysis[0])
    
    #print days to csv file
    import csv
    
    day = [day.split(' ',1)[0] for day in date_analysis]
    
    with open('days.csv','wb') as resultFile:
        writer = csv.writer(resultFile, delimiter=' ')
        writer.writerows(day)
        
    with open('week_days.csv','wb') as resultFile:
        writer = csv.writer(resultFile, delimiter=' ')
        writer.writerows(day_analysis)    