def dodle(f, stmt):
    f(stmt)
    f(stmt)

def say(stmt):
    print stmt

times = 10
stmt = 'Ola'

dodle(say, stmt)
