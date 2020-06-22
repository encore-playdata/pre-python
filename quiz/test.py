class Card:

    def __init__(self):

        self.card = 0

        print(' 카드가 발급 되었습니다')

    def charge(self, num):

        self.card += num

        print('%d 원이 충전되었습니다.' % num)

    def consume(self, num, place):

        if self.card >= num:

            self.card -= num

            print('%s 에서 %d 를 사용했습니다.' % (place, num))

        else:

            print('잔액이 부족합니다.')

    def print(self):

        print('%d 원 남았습니다.' % self.card)


class Movie_card(Card):

    def consume(self, num, place):

        if place == '영화관':

            num = 0.8 * num

            if self.card >= num:

                self.card -= num

                print('%s 에서 %d 를 사용했습니다.' % (place, num))

            else:

                print('잔액이 부족합니다.')


class Mart_card(Card):

    def consume(self, num, place):

        if place == '마트':

            num = round(num * 0.9)

            if self.card >= num:

                print('{}에서 {}원 사용했습니다.  '.format(place, num))

                self.card -= num

            else:

                print('잔액이 부족합니다')


class movie_mart_trans_card(Movie_card, Mart_card):

    def consume(self, num, place):

        if place in ['영화관', '마트']:

            Movie_card.consume(self, num, place)

            Mart_card.consume(self, num, place)

        else:

            if place == '교통':

                num = round(num * 0.9)

                if self.card >= num:

                    print('{}에서 {}원 사용했습니다.  '.format(place, num))

                    self.card -= num

                else:

                    print('잔액이 부족합니다')

            else:

                if self.card >= num:

                    print('{}에서 {}원 사용했습니다.  '.format(place, num))

                    self.card -= num

                else:

                    print('잔액이 부족합니다')

t_card1 = movie_mart_trans_card()

t_card1.charge(20000)

t_card1.consume(10000, '마트')

t_card1.consume(10000, '아무거나')

t_card1.print()