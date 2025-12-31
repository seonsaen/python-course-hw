from typing import List
from models.user import User


def select_top_users_by_rate(users: List[User], top_size: int = 5) -> List[User]:
    sorted_users = sorted(users, key=lambda u: u.rate, reverse=True)
    return sorted_users[:top_size]