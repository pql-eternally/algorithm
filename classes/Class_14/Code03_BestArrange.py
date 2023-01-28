"""
一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲，给你每一个项目开始的时间和结束的时间
你来安排宣讲的日程，要求会议室进行的宣讲的场次最多，返回最多的宣讲场次
"""
import random


class Program:
    start_at: int
    end_at: int

    def __init__(self, s: int, e: int):
        self.start_at = s
        self.end_at = e

    def __lt__(self, other):
        return self.end_at < other.end_at

    def __str__(self):
        return f'[{self.start_at}, {self.end_at}]'


def best_arrange(programs):
    programs.sort()
    time_line = 0
    count = 0
    for program in programs:
        if program.start_at < time_line:
            continue
        time_line = program.end_at
        count += 1
    return count


def generator_programs(program_size: int, max_time: int):
    programs = []
    for i in range(random.randint(1, program_size)):
        t1 = random.randint(1, max_time)
        t2 = random.randint(1, max_time)
        if t1 == t2:
            start_at, end_at = t1, t2 + 1
        else:
            start_at, end_at = min(t1, t2), max(t1, t2)
        programs.append(Program(start_at, end_at))
    return programs


def print_programs(programs: list):
    for program in programs:
        print(program, end=',')
    print()


def main():
    programs = generator_programs(5, 20)
    print_programs(programs)
    count = best_arrange(programs)
    print(count)


if __name__ == '__main__':
    main()
