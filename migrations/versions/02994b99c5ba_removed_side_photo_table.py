"""removed side photo table

Revision ID: 02994b99c5ba
Revises: 3bdcf51eceac
Create Date: 2019-05-11 11:46:32.084804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '02994b99c5ba'
down_revision = '3bdcf51eceac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sidephoto')
    op.drop_table('sidephotosmall')
    op.add_column('content', sa.Column('update_date', sa.DateTime(), nullable=False))
    op.drop_column('content', 'create_date')
    op.drop_column('page', 'create_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page', sa.Column('create_date', mysql.DATETIME(), nullable=False))
    op.add_column('content', sa.Column('create_date', mysql.DATETIME(), nullable=False))
    op.drop_column('content', 'update_date')
    op.create_table('sidephotosmall',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('file_size', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('file_width', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('file_height', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('page_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('create_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['page_id'], ['page.id'], name='sidephotosmall_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('sidephoto',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('file_size', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('file_width', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('file_height', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('sidephotosmall_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('create_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['sidephotosmall_id'], ['sidephotosmall.id'], name='sidephoto_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
