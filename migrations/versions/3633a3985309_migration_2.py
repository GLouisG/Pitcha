"""Migration 2

Revision ID: 3633a3985309
Revises: d6a6b4882a13
Create Date: 2021-09-20 22:48:39.141419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3633a3985309'
down_revision = 'd6a6b4882a13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('downvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('downvotess')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('downvotess',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='downvotess_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='downvotess_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='downvotess_pkey')
    )
    op.drop_table('downvotes')
    # ### end Alembic commands ###
