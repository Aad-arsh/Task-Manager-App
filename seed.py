# Seed script to create a test user and some tasks
from task_manager import create_app
from task_manager.extensions import db
from task_manager.models import User, Task, Category
from datetime import date, timedelta

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(email="test@example.com")
    user.set_password("password")
    db.session.add(user)

    work = Category(name="Work")
    personal = Category(name="Personal")
    db.session.add_all([work, personal])
    db.session.commit()

    t1 = Task(title="Finish report", description="Quarterly numbers",
              priority="High", status="In Progress",
              due_date=date.today() + timedelta(days=2), user_id=user.id, category_id=work.id)
    t2 = Task(title="Buy groceries", description="Milk, eggs, bread",
              priority="Medium", status="Pending",
              due_date=date.today() + timedelta(days=1), user_id=user.id, category_id=personal.id)
    t3 = Task(title="Gym", description="Leg day",
              priority="Low", status="Pending",
              due_date=None, user_id=user.id, category_id=personal.id)
    db.session.add_all([t1, t2, t3])
    db.session.commit()

    print("Seeded: user test@example.com / password")
