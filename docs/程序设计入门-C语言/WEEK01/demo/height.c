# include <stdio.h>
# 05/04/20 21:41

int main()
{
    printf("��������ߵ�Ӣ���Ӣ�磺");
    int foot;
    int inch;
    scanf("%d %d", &foot, &inch);
    printf("�����%f�ס�\n", ((foot + inch / 12.0) * 0.3048));
    return 0;
}
