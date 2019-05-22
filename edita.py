# -*- coding: utf-8 -*-

import datetime
import os
import random
import sys
from time import sleep

def ________util________():
    pass

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def get_lastmodified_nanotime(filename):
    stat_result = os.stat(filename)
    return stat_result.st_mtime_ns

def get_now_by_dt():
    """ @return A datetime object """
    return datetime.datetime.now()

def diff_microseconds_between_dt_and_dt(dt_future, dt_past):
    delta = dt_future - dt_past
    microseconds = delta / datetime.timedelta(microseconds=1)
    return microseconds

def ________edita_common________():
    pass

def _select_word_randomly_from_wordlines(wordlines, count):
    # random.randint(x,y): interger between [x, y)
    range_lower = 0
    range_upper = len(wordlines)

    selected_wordlines = []
    for i in range(count):
        idx = random.randint(range_lower, range_upper)
        word = wordlines[idx]
        selected_wordlines.append(word)

    return selected_wordlines

def _to_upper_randomly(line, count):
    # Pick replaceee indexes firstly to avoid picking duplicates
    replaced_index_targets = [i for i in range(0, len(line))]
    replaced_indexes = []
    while True:
        i = random.randint(0, len(replaced_index_targets))
        replaced_idx_candidate = replaced_index_targets[i]

        peeked = line[replaced_idx_candidate]
        if peeked.isupper():
            continue
        if peeked == ' ':
            continue

        replaced_indexes.append(replaced_idx_candidate)
        replaced_index_targets.remove(replaced_idx_candidate)
        if(len(replaced_indexes) >= count):
            break

    replaced_line = line
    for i in range(len(replaced_indexes)):
        idx = replaced_indexes[i]

        # Need to convert to list because TypeError: 'str' object does not support item assignment
        replaced_line = list(replaced_line)
        replaced_line[idx] = replaced_line[idx].upper()
        replaced_line = ''.join(replaced_line)

    return replaced_line

def create_stage(wordlines, stage_xsize, stage_ysize, stage_replacecount):
    ''' return [correct_stagelines, initial_stagelines] '''
    stage_length = stage_xsize * stage_ysize

    stageline = ''
    while True:
        word = _select_word_randomly_from_wordlines(wordlines, 1)[0]

        if len(stageline)==0:
            stageline = word
        else:
            stageline = '{} {}'.format(stageline, word)

        if len(stageline) >= stage_length:
            break

    stageline_editted = _to_upper_randomly(stageline, stage_replacecount)

    correct_stagelines = []
    initial_stagelines = []
    for i in range(stage_ysize):
        start = i * stage_xsize
        end = start + stage_xsize
        line = stageline_editted[start:end]
        initial_stagelines.append(line)

        correct_line = stageline[start:end]
        correct_stagelines.append(correct_line)

    return [correct_stagelines, initial_stagelines]

def write_stage_to_tempfile(tempfilename, stagelines):
    list2file(tempfilename, stagelines)

def judge_stage(correct_stagelines, your_current_stagelines):
    correct = "".join(correct_stagelines)
    current = "".join(your_current_stagelines)
    if args.debug:
        print('correct:"{}"'.format(correct))
        print('current:"{}"'.format(current))
    return correct == current

def convert_microseconds_to_edita_score_float(microseconds_by_float):
    # dt1 = get_now_by_dt()
    # sleep(1.5)
    # dt2 = get_now_by_dt()
    # ms = diff_microseconds_between_dt_and_dt(dt2, dt1)
    # print(ms) 
    #    -> 1513190.0
    #
    #       1      <- too rough
    #       1.5    <- rough a little
    #       1.51   <= I chooose you!
    #       1.513  <- too grain
    return round(microseconds_by_float/1000000, 2)

def print_without_linebreak(*args):
    # There is an output buffering sometimes on my env especially end='' case,
    # so explicit flush everytime.
    print(*args, end='')
    sys.stdout.flush()

def ________edita_args________():
    pass

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-w', '--wordlist', type=str, required=True)
    parser.add_argument('-t', '--tempfile', type=str, default='edita.temp')

    parser.add_argument('-x', '--xsize', type=int, default=32)
    parser.add_argument('-y', '--ysize', type=int, default=10)
    parser.add_argument('-r', '--replacecount', type=int, default=10)

    parser.add_argument('-c', '--gamecount', type=int, default=3)

    parser.add_argument('--debug', default=False, action='store_true')

    args = parser.parse_args()
    return args

def ________main________():
    pass

args = parse_arguments()

wordlines = file2list(args.wordlist)
tempfilename = args.tempfile
X = args.xsize
Y = args.ysize
L = X*Y
REPLACECOUNT = args.replacecount
GAMECOUNT = args.gamecount

print('==== edita.py ====')

current_stagecount = 1
your_total_seconds = 0.0
while True:
    correct_stagelines, initial_stagelines = create_stage(wordlines, X, Y, REPLACECOUNT)
    write_stage_to_tempfile(tempfilename, initial_stagelines)
    start_dt = get_now_by_dt()

    print_without_linebreak('Stage.{:02d}:'.format(current_stagecount))

    cur_ns = get_lastmodified_nanotime(tempfilename)
    while True:
        sleep(0.01)
        latest_ns = get_lastmodified_nanotime(tempfilename)
        if latest_ns == cur_ns:
            continue
        cur_ns = latest_ns

        your_current_stagelines = file2list(tempfilename)
        is_correct_your_edit = judge_stage(correct_stagelines, your_current_stagelines)
        if not(is_correct_your_edit):
            print_without_linebreak('x')
            continue

        end_dt = get_now_by_dt()
        your_microseconds = diff_microseconds_between_dt_and_dt(end_dt, start_dt)
        your_seconds = convert_microseconds_to_edita_score_float(your_microseconds)
        your_total_seconds += your_seconds
        print('')
        print('         {} sec.'.format(your_seconds))
        break

    current_stagecount += 1
    if(current_stagecount > GAMECOUNT):
        break

print('         ----')
print('   Total:{} sec.'.format(your_total_seconds))
