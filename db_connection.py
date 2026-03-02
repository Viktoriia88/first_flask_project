from sqlalchemy import create_engine, String, ForeignKey, delete
from sqlalchemy.orm import DeclarativeBase, relationship, Session, Mapped, mapped_column

engine = create_engine('sqlite:///database.db')

class Base(DeclarativeBase):
    pass

class Employees(Base):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column( primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    position: Mapped[str] = mapped_column(String(255), nullable=False)
    project: Mapped['Project'] = relationship(back_populates='employees')

class Project(Base):
    __tablename__ = 'project'

    id: Mapped[int] = mapped_column(primary_key=True)
    project_name: Mapped[str] = mapped_column(String(255), nullable=False)
    employee_id: Mapped[int] = mapped_column(ForeignKey(Employees.id, ondelete="CASCADE"), nullable=False)
    employees: Mapped['Employees'] = relationship( back_populates='project')

Base.metadata.create_all(engine)

with Session(engine) as session:
    row = Employees(name='Viktoriia', position='Developer')
    row.project = Project(project_name='Web application')
    session.add(row)
    session.commit()

# with Session(engine) as session:
#     employees = session.scalars(select(Employees.name)).all()

# with Session(engine) as session:
#     session.execute(delete(Project))
#     session.execute(delete(Employees))
#     session.commit()

