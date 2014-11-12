#!/usr/bin/python

import os, subprocess, webbrowser

path = os.path.dirname(os.path.realpath(__file__))

def main():
    # Open a file
    testCaseDir = os.path.join(path, '../testCases')
    testCaseFiles = os.listdir(testCaseDir)
    create_html_table()

    # Iterate across all the testcases
    for file in testCaseFiles:
        if file.endswith('.txt'):
            infile = open(os.path.join(testCaseDir, file), 'r')
            contents = infile.read().split('\n')
            infile.close()
            proc = subprocess.Popen(['python', os.path.join(path, '../testCaseExecutables', contents[2]), contents[3], contents[4], contents[5]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdoutValue = proc.communicate()[0]
            stdoutValue = stdoutValue[:-1]
            if(stdoutValue == contents[6]):
                print 'pass'
                contents.append('Passed')
            else:
                print 'fail'
                contents.append('Failed')
            add_row_to_table(contents, stdoutValue)
    end_html_table()

    webbrowser.open('file://'+os.path.join(path, '../reports/report.html'))


def create_html_table():
    outfile = open(os.path.join(path, '../reports/report.html'), 'w')
    infile = open(os.path.join(path, '../reportHelpers/startingHtml.html'), 'r')
    startingHtml = infile.read()
    infile.close()
    outfile.write(startingHtml)
    outfile.close()

def end_html_table():
    outfile = open(os.path.join(path, '../reports/report.html'), 'a')
    infile = open(os.path.join(path, '../reportHelpers/endingHtml.html'), 'r')
    endingHtml = infile.read()
    infile.close()
    outfile.write(endingHtml)
    outfile.close()

def add_row_to_table(columns, res):
    outfile = open(os.path.join(path, '../reports/report.html'), 'a')

    outfile.write('<tr>')
    outfile.write('<td>'+columns[0]+'</td>')
    outfile.write('<td><a href="#" data-tooltip="'+columns[1]+'"><img src="../reportHelpers/img/icon.png" height=40px /></a></td>')
    outfile.write('<td>'+columns[3]+'</td>')
    outfile.write('<td>'+columns[4]+'</td>')
    outfile.write('<td>'+columns[5]+'</td>')
    outfile.write('<td>'+columns[6]+'</td>')
    outfile.write('<td>'+res+'</td>')
    if(columns[7] == 'Passed'):
        outfile.write('<td class="passed">'+columns[7]+'</td>')
    else:
        outfile.write('<td class="failed">'+columns[7]+'</td>')
    outfile.write('</tr>')






if __name__ == '__main__':
    main()
    