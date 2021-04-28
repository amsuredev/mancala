class ContainerStones:
    def __init__(self,index, num_stones=None, type=None):
        self.index = index
        if type is None:
            self.type = "dolka"
        else:
            self.type = type
        if num_stones is None:
            self.num_stones = 4
        else:
            self.num_stones = num_stones

    def __str__(self):
        return str(self.num_stones)

class Player:
    def __init__(self, containters=None, id='a'):
        self.id = id
        if containters is None:
            self.containers = [ContainerStones(0), ContainerStones(1), ContainerStones(2), ContainerStones(3), ContainerStones(4), ContainerStones(5), ContainerStones(6, 0, type="studnia")]
        else:
            self.containers = containters

    def __eq__(self, other):
        return self.id == other.id


class Mancala:
    def __init__(self, player_a=None, player_b=None, whose_move=None):
        if player_a is None:
            self.player_a = Player()
        else:
            self.player_a = player_a

        if player_b is None:
            self.player_b = Player(id='b')
        else:
            self.player_b = player_b

        if whose_move is None:
            self.whose_move = self.player_b
        else:
            self.whose_move = whose_move

        self.finish = False


    def step_player(self, container_ind, person_letter):
        if person_letter == self.whose_move.id:
            self.step(container_ind)
        else:
            print("step of another player")

    def step(self, container_ind):
        if container_ind == 6 or self.whose_move.containers[container_ind].num_stones == 0:
            return
        current_player = self.whose_move
        stones_num = current_player.containers[container_ind].num_stones
        current_player.containers[container_ind].num_stones = 0
        container = current_player.containers[container_ind]
        for stone in range(stones_num):
            current_player, container = self.next_container(current_player, container)
            if container.type == "studnia" and current_player != self.whose_move:
                current_player, container = self.next_container(current_player, container)
            container.num_stones += 1
        self.__make_beating_if_exist(container, current_player)
        if not (self.whose_move == current_player and container.index == 6):
            self.whose_move = self.player_b if self.whose_move == self.player_a else self.player_a

        if self.__check_if_end_game():
            self.__finish_game()
            return

    def next_container(self, current_player, container):
        container_ind = container.index
        if container_ind != 6:
            return current_player, current_player.containers[container_ind + 1]
        else:
            current_player = self.player_b if current_player == self.player_a else self.player_a
            return current_player, current_player.containers[0]

    def __make_beating_if_exist(self, container, current_player):
        if container.num_stones == 1 and container.index != 6:
            another_player = self.player_b if self.whose_move == self.player_a else self.player_a
            if self.whose_move == current_player:
                another_player_container = another_player.containers[5 - container.index]
                if another_player_container.num_stones != 0:
                    self.whose_move.containers[6].num_stones += container.num_stones + another_player_container.num_stones
                    container.num_stones = 0
                    another_player_container.num_stones = 0

    def __check_if_end_game(self):
        for container_ind in range(len(self.whose_move.containers) - 1):
            if self.whose_move.containers[container_ind].num_stones != 0:
                return False
        return True

    def __finish_game(self):
        another_player = self.player_b if self.whose_move == self.player_a else self.player_a
        to_add = 0
        for index in range(len(another_player.containers) - 1):
            to_add += another_player.containers[index].num_stones
            another_player.containers[index].num_stones = 0
        another_player.containers[-1].num_stones += to_add
        self.finish = True

