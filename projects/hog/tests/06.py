test = {
  'name': 'Question 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Another commentary function.',
          'choices': [
            'Another commentary function.',
            'An integer representing the score.',
            'None.'
          ],
          'hidden': False,
          'locked': False,
          'question': 'What does a commentary function return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=5, say=echo)
          3 0
          3 3
          6 3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> def count(n):
          ...     def say(s0, s1):
          ...         print(n, s0)
          ...         return count(n + 1)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=10, say=count(1))
          1 5
          2 5
          3 10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return echo
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          4 0
          4 12
          8 12
          8 24
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
          accd0f5c57e0f3fad13791aaecafc38b
          c42887e7b9ffe8fc26bb57b61329f916
          cbe9649db9e3fa2aa95c8f2df21707e5
          26dad951f8e75106f151e4085e117edd
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Ensure that say is properly updated within the body of play even with extra turns
          >>> def total(s0, s1):
          ...     print(s0 + s1)
          ...     return echo
          >>> def echo(s0, s1):
          ...     print(s0, s1)
          ...     return total
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(8, 2), goal=20, say=echo)
          9b66e3dd695a56bd11068cfde738be54
          70e71b420a966665c548a3bb2cb30d7d
          22ba4e8c1bbee261318d242bca9d3e22
          1b69dde49f2d00e5909950f5df0efdd9
          3cea65769a2f01cdbea7cfca5f7c5147
          506685ee432959c29851e24ca582d576
          52c81c85ebf386bc88406a835c7ea55a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1):
          ...     print('*', s0)
          ...     return echo_0
          >>> def echo_1(s0, s1):
          ...     print('**', s1)
          ...     return echo_1
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=3, say=both(echo_0, echo_1))
          3f321d5ce997d2f3989685f56de8bdce
          4a64fe964dc771a219ed773c3a146c75
          3f321d5ce997d2f3989685f56de8bdce
          e4010b4a7d51e81cc1f49e08b015b8eb
          a6ba27fb33805545324a96eadcd30897
          e4010b4a7d51e81cc1f49e08b015b8eb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes()))
          Player 0 now has 1 and Player 1 now has 0
          Player 0 takes the lead by 1
          Player 0 now has 1 and Player 1 now has 1
          Player 0 now has 2 and Player 1 now has 1
          Player 0 takes the lead by 1
          Player 0 now has 2 and Player 1 now has 9
          Player 1 takes the lead by 7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
