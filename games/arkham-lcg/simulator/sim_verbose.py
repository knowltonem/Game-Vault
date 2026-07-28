import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

from engine.game import Game

game = Game(['eleanor_heart', 'the_man_in_black'], 'spreading_flames', 'standard')
result = game.run(max_rounds=30)

print()
print('=' * 60)
print('FINAL RESULT')
print('=' * 60)
print(result)
print('Reason:', game.game_over_reason)
act_name = game.game_state.current_act.name if game.game_state.current_act else 'None'
print('Act:', act_name)
print('Clues gathered:', game.game_state.clues_gathered)
print('Servant defeated:', game.game_state.servant_of_flame_defeated)
print()
for inv in game.game_state.investigators:
    status = 'DEFEATED' if inv.is_defeated() else 'ALIVE'
    print(f'{inv.name} [{status}]:')
    print(f'  HP {inv.current_health}/{inv.health} | SAN {inv.current_sanity}/{inv.sanity}')
    print(f'  Resources: {inv.resources}')
    hand_names = [f'[{c.name}]' for c in inv.hand]
    print(f'  Hand ({len(inv.hand)}): {", ".join(hand_names)}')
    play_names = [f'[{c.name}]' for c in inv.play_area]
    print(f'  In play ({len(inv.play_area)}): {", ".join(play_names)}')
    engaged = [e.name for e in inv.engaged_enemies]
    print(f'  Engaged: {engaged if engaged else "none"}')
