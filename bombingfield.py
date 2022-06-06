bombingfield = [['∧'] * 10 for i in range(10)]

def bombing(p, q):
  bombingfield[p][q] = 'O '
  if p!=0 :
    bombingfield[p-1][q] = 'O '
  if p!=9 :
    bombingfield[p+1][q] = 'O '
  if q!=0 :
    bombingfield[p][q-1] = 'O '
  if q!=9 :
    bombingfield[p][q+1] = 'O '

  for i in range(10):
    for j in range(10):
        print(bombingfield[i][j], end=' ')
    print(end = '\n')


num = int(input('포격 게임!\n폭탄을 투여할 횟수 '))
for i in range(num):
  bombing(int(input('x좌표')), int(input('y좌표')))
