'''
Provide match related biz model.

export only Match class right now.
'''


class Match:
    '''
    Match model.
    '''
    def __init__(self, **args):
        match_keys = (
            'id',
            'home_team',
            'visit_team',
            'home_score',
            'visit_score',
            'period_cn'
        )
        for key in match_keys:
            self.__dict__[key] = args[key].replace('\n', '')

    def __repr__(self):
        return (
            '{match.id} {match.home_team} {match.home_score}'
            ' - '
            '{match.visit_score}{match.visit_team} {match.period_cn}'
        ).format(match=self)
