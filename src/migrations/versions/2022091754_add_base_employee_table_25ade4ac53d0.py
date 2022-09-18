"""add base employee table

Revision ID: 25ade4ac53d0
Revises: 
Create Date: 2022-09-17 19:54:28.060305

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision = '25ade4ac53d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('first_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('patronymic_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('post', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('employment_date', sa.DateTime(), nullable=False),
    sa.Column('salary', sa.Numeric(), nullable=False),
    sa.Column('chief_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###