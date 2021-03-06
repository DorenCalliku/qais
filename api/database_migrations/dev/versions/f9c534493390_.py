"""empty message

Revision ID: f9c534493390
Revises: 
Create Date: 2021-05-28 22:11:39.503350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9c534493390'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('competence', sa.Integer(), nullable=True),
    sa.Column('network_ability', sa.Integer(), nullable=True),
    sa.Column('promoted', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prediction_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('archived', sa.Boolean(), nullable=True),
    sa.Column('page', sa.Integer(), nullable=True),
    sa.Column('instance_count', sa.Integer(), nullable=True),
    sa.Column('accuracy', sa.Float(), nullable=True),
    sa.Column('parameters', sa.JSON(), nullable=True),
    sa.Column('model_type', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('train_size', sa.Integer(), nullable=True),
    sa.Column('train_pos', sa.Integer(), nullable=True),
    sa.Column('train_time', sa.Float(), nullable=True),
    sa.Column('test_pos', sa.Integer(), nullable=True),
    sa.Column('test_time', sa.Float(), nullable=True),
    sa.Column('pickle_obj', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_prediction_model_timestamp'), 'prediction_model', ['timestamp'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.Column('pm_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pm_id'], ['prediction_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_name'), 'task', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_name'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_prediction_model_timestamp'), table_name='prediction_model')
    op.drop_table('prediction_model')
    op.drop_table('instance')
    # ### end Alembic commands ###
