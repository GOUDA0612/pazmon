#インポート

#グローバル変数の宣言
ELEMENT_SYMBOLS ={
        '火' : '$',
        '水' : '~',
        '風' : '@',
        '土' : '#',
        '命' : '&',
        '無' : ' ',
}
ELEMENT_COLORS ={
        '火' : 1,
        '水' : 6,
        '風' : 2,
        '土' : 3,
        '命' : 5,
        '無' : 7,
}
#関数宣言


def main():
<<<<<<< HEAD
=======
    friends = [
            {
                'name' : '青龍',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '風',
                'ap' : 15,
                'dp' : 10
            },
            {
                'name' : '朱雀',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '火',
                'ap' : 15,
                'dp' : 10
            },
            {
                'name' : '白虎',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '土',
                'ap' : 20,
                'dp' : 5
            },
            {
                'name' : '玄武',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '水',
                'ap' : 20,
                'dp' : 15
            },
            
    ]
>>>>>>> d5c273c (friends 追加（修正）)
    monster_list = [
            {
                'name' : 'スライム',
                'hp' : 100,
                'max_hp' : 100,
                'element' : '水',
                'ap' : 10,
                'dp' : 1
            },
            {
                'name' : 'ゴブリン',
                'hp' : 200,
                'max_hp' : 200,
                'element' : '土',
                'ap' : 20,
                'dp' : 5
            },
            {
                'name' : 'オオコウモリ',
                'hp' : 300,
                'max_hp' : 300,
                'element' : '風',
                'ap' : 30,
                'dp' : 10
            },
            {
                'name' : 'ウェアウルフ',
                'hp' : 400,
                'max_hp' : 400,
                'element' : '風',
                'ap' : 40,
                'dp' : 15
            },
            {
                'name' : 'ドラゴン',
                'hp' : 600,
                'max_hp' : 600,
                'element' : '火',
                'ap' : 50,
                'dp' :20 
            },
    ]
    friends = [
            {
                'name' : '青龍',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '風',
                'ap' : 15,
                'dp' :10 
            }, 
            {
                'name' : '朱雀',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '火',
                'ap' : 25,
                'dp' :10 
            }, 
            {
                'name' : '白虎',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '風',
                'ap' : 20,
                'dp' :5 
            }, 
            {
                'name' : '玄武',
                'hp' : 150,
                'max_hp' : 150,
                'element' : '水',
                'ap' : 20,
                'dp' :15 
            }, 
    ]
    while True:
        player_name = input('プレイヤー名を入力してください>>')
        if len(player_name) > 0:
            break
        print('エラー:プレイヤー名を入力してください')

    print('***puzle&monster***')
<<<<<<< HEAD
    print(f'{player_name}のHP:600')
    print(f'{player_name}のパーティを編成しました!')
    print_friends(friends)

    kills = go_dungeon(player_name,monster_list)
=======
    party = organize_party(player_name,friends)
    kills = go_dungeon(party,monster_list)
>>>>>>> d5c273c (friends 追加（修正）)
    if kills == len(monster_list):
        print('*** GAME CLEARED!! ***')
    else:
        print('*** GAME OVER!! ***')

    print(f'倒したモンスター数 = {kills}')
    
def print_friends(friends):
    print('<パーティ編成>--------------------')
    for member in friends:
        print_monster_name(member)
        print(f' HP:{member["hp"]} 攻撃:{member["ap"]} DP:{member["dp"]}')
    print('----------------------------------')

def go_dungeon(player_name,monster_list):
    kills = 0
<<<<<<< HEAD
    for monster in monster_list:
        kills += do_battle(monster)

        if kills < len(monster_list):
            print(f'{player_name}はさらに奥へと進んだ...')
        print('==================================')
プレイヤー名を入力してください>>a
***puzle&monster***
aのHP:600
aのパーティを編成しました!
<パーティ編成>--------------------
@青龍@ HP:150 攻撃:15 DP:10
$朱雀$ HP:150 攻撃:25 DP:10
@白虎@ HP:150 攻撃:20 DP:5
~玄武~ HP:150 攻撃:20 DP:15
----------------------------------
~スライム~が現れた!
~スライム~を倒した!

aはさらに奥へと進んだ...

==================================
#ゴブリン#が現れた!
#ゴブリン#を倒した!

aはさらに奥へと進んだ...

==================================
@オオコウモリ@が現れた!
@オオコウモリ@を倒した!

aはさらに奥へと進んだ...

==================================
@ウェアウルフ@が現れた!
@ウェアウルフ@を倒した!

aはさらに奥へと進んだ...

==================================
$ドラゴン$が現れた!
$ドラゴン$を倒した!
==================================
aはダンジョンを制覇した
*** GAME CLEARED!! ***
倒したモンスター数 = 5

Press ENTER or type command to continue
    print(f'{player_name}はダンジョンを制覇した')
=======
    print(f'{party['name']}のパーティ(HP={party['hp']})はダンジョンに到着した')
    show_party(party)
    for monster in monster_list:
        kills += do_battle(monster)
        if party['hp']<= 0:
            print(f'{party['name']}はダンジョンから逃げ出した')
            break
        print(f'{party['name']}はさらに奥に進んだ')
        print('================================')
    else:
        print(f'{party['name']}はダンジョンを制覇した')


>>>>>>> d5c273c (friends 追加（修正）)
    return kills 

def do_battle(monster):
    print():
    print_monster_name(monster)
    print('が現れた!')
    print_monster_name(monster)
    print('を倒した!')
    return 1

def print_monster_name(monster):
    monster_name = monster['name']
    symbol = ELEMENT_SYMBOLS[monster['element']]
    color = ELEMENT_COLORS[monster['element']]

    #モンスター名を表示
    print(f'\033[3{color}m{symbol}{monster_name}{symbol}\033[0m',end = '')

<<<<<<< HEAD
=======
def organize_party(player_name,friends):
    total_hp = 0
    total_dp = 0
    for friend in friends:
        total_hp += friend['hp']
        total_hp += friend['dp']

    party = {
            'name':player_name,
            'friends':friends,
            'hp':total_hp,
            'max_hp':total_hp,
            'dp':total_dp /len(friends)
    }
    return party

def show_party(party):
    print('<パーティ編成>---------------------')
    for friend in party['friends']:
        print_monster_name(friend)
        print(f' HP = {friend['hp']} 攻撃={friend['ap']} 防御 = {friend['dp']}')
    print('-----------------------------------')
    print()




>>>>>>> d5c273c (friends 追加（修正）)
# main関数の呼び出し
main()
