from roles import get_user_role

test_users = [123456789, 987654321, 555555555, 111222333]  # el último no está en ROLES

for user in test_users:
    role = get_user_role(user)
    print(f"User {user} tiene rol: {role}")

