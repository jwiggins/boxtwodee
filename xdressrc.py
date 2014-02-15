from os.path import join
from xdress.utils import apiname

_from_src_dir = lambda x: join('Box2D', 'Box2D', *x.split('/'))

def _api_name_kwargs(src_file_glob):
    return {'srcfiles': _from_src_dir(src_file_glob),
            'incfiles': 'Box2D.h',
            'language': 'c++',
    }

package = 'boxtwodee'
packagedir = 'boxtwodee'
includes = [join('.', 'Box2D'), join('.', 'Box2D', 'Box2D'),
            _from_src_dir('Common'),
            _from_src_dir('Collision'), _from_src_dir('Collision/Shapes'),
            _from_src_dir('Dynamics'), _from_src_dir('Dynamics/Contacts'),
            _from_src_dir('Dynamics/Joints'),
            _from_src_dir('Rope')]

plugins = ('xdress.autoall', 'xdress.pep8names', 'xdress.cythongen',)

extra_types = 'boxtwodee_extra_types'  # non-default value

dtypes = [
    'int8', 'int16', 'int32',
    'uint8', 'uint16', 'uint32',
    'float32', 'float64',
    'b2AABB', 'b2Block', 'b2BodyDef', 'b2Chunk', 'b2ClipVertex', 'b2Color',
    'b2ContactEdge', 'b2ContactFeature', 'b2ContactImpulse',
    'b2ContactPositionConstraint', 'b2ContactRegister', 'b2ContactSolverDef',
    'b2ContactVelocityConstraint', 'b2DistanceInput', 'b2DistanceJointDef',
    'b2DistanceOutput', 'b2DistanceProxy', 'b2EPAxis', 'b2EPCollider',
    'b2Filter', 'b2FixtureDef', 'b2FixtureProxy', 'b2FrictionJointDef',
    'b2GearJointDef', 'b2Jacobian', 'b2JointDef', 'b2JointEdge', 'b2Manifold',
    'b2ManifoldPoint', 'b2MassData', 'b2Mat22', 'b2Mat33', 'b2MotorJointDef',
    'b2MouseJointDef', 'b2Pair', 'b2Position', 'b2PositionSolverManifold',
    'b2PrismaticJointDef', 'b2Profile', 'b2PulleyJointDef', 'b2RayCastInput',
    'b2RayCastOutput', 'b2ReferenceFace', 'b2RevoluteJointDef', 'b2RopeDef',
    'b2RopeJointDef', 'b2Rot', 'b2SeparationFunction', 'b2Simplex',
    'b2SimplexCache', 'b2SimplexVertex', 'b2SolverData', 'b2StackEntry',
    'b2Sweep', 'b2TempPolygon', 'b2TimeStep', 'b2TOIInput', 'b2TOIOutput',
    'b2Transform', 'b2TreeNode', 'b2Vec2', 'b2Vec3', 'b2Velocity',
    'b2VelocityConstraintPoint', 'b2Version', 'b2WeldJointDef',
    'b2WheelJointDef', 'b2WorldManifold', 'b2WorldQueryWrapper',
    'b2WorldRayCastWrapper',
]

stlcontainers = []

dtypes_module = 'dt'
stlcontainers_module = 'stlc'
variables = []

functions = []

classes = [
    # Structs
    apiname('b2AABB', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2Block', **_api_name_kwargs('Common/b2BlockAllocator*')),
    apiname('b2BodyDef', **_api_name_kwargs('Dynamics/b2Body*')),
    apiname('b2Chunk', **_api_name_kwargs('Common/b2BlockAllocator*')),
    apiname('b2ClipVertex', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2Color', **_api_name_kwargs('Common/b2Draw*')),
    apiname('b2ContactEdge',
            **_api_name_kwargs('Dynamics/Contacts/b2Contact*')),
    apiname('b2ContactFeature', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2ContactImpulse',
            **_api_name_kwargs('Dynamics/b2WorldCallbacks*')),
    apiname('b2ContactPositionConstraint',
            **_api_name_kwargs('Dynamics/Contacts/b2ContactSolver*')),
    apiname('b2ContactRegister',
            **_api_name_kwargs('Dynamics/Contacts/b2Contact*')),
    apiname('b2ContactSolverDef',
            **_api_name_kwargs('Dynamics/Contacts/b2ContactSolver*')),
    apiname('b2ContactVelocityConstraint',
            **_api_name_kwargs('Dynamics/Contacts/b2ContactSolver*')),
    apiname('b2DistanceInput', **_api_name_kwargs('Collision/b2Distance*')),
    apiname('b2DistanceJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2DistanceJoint*')),
    apiname('b2DistanceOutput', **_api_name_kwargs('Collision/b2Distance*')),
    apiname('b2DistanceProxy', **_api_name_kwargs('Collision/b2Distance*')),
    apiname('b2EPAxis', **_api_name_kwargs('Collision/b2CollideEdge*')),
    apiname('b2EPCollider', **_api_name_kwargs('Collision/b2CollideEdge*')),
    apiname('b2Filter', **_api_name_kwargs('Dynamics/b2Fixture*')),
    apiname('b2FixtureDef', **_api_name_kwargs('Dynamics/b2Body*')),
    apiname('b2FixtureProxy', **_api_name_kwargs('Dynamics/b2Fixture*')),
    apiname('b2FrictionJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2FrictionJoint*')),
    apiname('b2GearJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2GearJoint*')),
    apiname('b2Jacobian', **_api_name_kwargs('Dynamics/Joints/b2Joint*')),
    apiname('b2JointDef', **_api_name_kwargs('Dynamics/Joints/b2Joint*')),
    apiname('b2JointEdge', **_api_name_kwargs('Dynamics/Joints/b2Joint*')),
    apiname('b2Manifold', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2ManifoldPoint', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2MassData', **_api_name_kwargs('Collision/Shapes/b2Shape*')),
    apiname('b2Mat22', **_api_name_kwargs('Common/b2Math*')),
    apiname('b2Mat33', **_api_name_kwargs('Common/b2Math*')),
    apiname('b2MotorJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2MotorJoint*')),
    apiname('b2MouseJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2MouseJoint*')),
    apiname('b2Pair', **_api_name_kwargs('Collision/b2BroadPhase*')),
    apiname('b2Position', **_api_name_kwargs('Dynamics/b2TimeStep*')),
    apiname('b2PositionSolverManifold',
            **_api_name_kwargs('Dynamics/Contacts/b2ContactSolver*')),
    apiname('b2PrismaticJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2PrismaticJoint*')),
    apiname('b2Profile', **_api_name_kwargs('Dynamics/b2TimeStep*')),
    apiname('b2PulleyJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2PulleyJoint*')),
    apiname('b2RayCastInput', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2RayCastOutput', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2ReferenceFace', **_api_name_kwargs('Collision/b2CollideEdge*')),
    apiname('b2RevoluteJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2RevoluteJoint*')),
    apiname('b2RopeDef', **_api_name_kwargs('Rope/b2Rope*')),
    apiname('b2RopeJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2RopeJoint*')),
    apiname('b2Rot', **_api_name_kwargs('Common/b2Math*')),
    apiname('b2SeparationFunction',
            **_api_name_kwargs('Collision/b2TimeOfImpact*')),
    apiname('b2Simplex', **_api_name_kwargs('Collision/b2Distance*')),
    apiname('b2SimplexCache', **_api_name_kwargs('Collision/b2Distance*')),
    apiname('b2SimplexVertex', **_api_name_kwargs('Collision/b2Distance*')),
    apiname('b2SolverData', **_api_name_kwargs('Dynamics/b2TimeStep*')),
    apiname('b2StackEntry', **_api_name_kwargs('Common/b2StackAllocator*')),
    apiname('b2Sweep', **_api_name_kwargs('Common/b2Math*')),
    apiname('b2TempPolygon', **_api_name_kwargs('Collision/b2CollideEdge*')),
    apiname('b2TimeStep', **_api_name_kwargs('Dynamics/b2TimeStep*')),
    apiname('b2TOIInput', **_api_name_kwargs('Collision/b2TimeOfImpact*')),
    apiname('b2TOIOutput', **_api_name_kwargs('Collision/b2TimeOfImpact*')),
    apiname('b2Transform', **_api_name_kwargs('Common/b2Math*')),
    apiname('b2TreeNode', **_api_name_kwargs('Collision/b2DynamicTree*')),
    apiname('b2Vec2', **_api_name_kwargs('Common/b2Math*')),
    apiname('b2Vec3', **_api_name_kwargs('Common/b2Math*')),
    apiname('b2Velocity', **_api_name_kwargs('Dynamics/b2TimeStep*')),
    apiname('b2VelocityConstraintPoint',
            **_api_name_kwargs('Dynamics/Contacts/b2ContactSolver*')),
    apiname('b2Version', **_api_name_kwargs('Common/b2Settings*')),
    apiname('b2WeldJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2WeldJoint*')),
    apiname('b2WheelJointDef',
            **_api_name_kwargs('Dynamics/Joints/b2WheelJoint*')),
    apiname('b2WorldManifold', **_api_name_kwargs('Collision/b2Collision*')),
    apiname('b2WorldQueryWrapper', **_api_name_kwargs('Dynamics/b2World*')),
    apiname('b2WorldRayCastWrapper', **_api_name_kwargs('Dynamics/b2World*')),


    # Classes
    apiname('b2BlockAllocator',
            **_api_name_kwargs('Common/b2BlockAllocator*')),
    apiname('b2Draw', **_api_name_kwargs('Common/b2Draw*')),
    apiname('b2StackAllocator',
            **_api_name_kwargs('Common/b2StackAllocator*')),
    apiname('b2Timer', **_api_name_kwargs('Common/b2Timer*')),
    apiname('b2Shape', **_api_name_kwargs('Collision/Shapes/b2Shape*')),
    apiname('b2ChainShape',
            **_api_name_kwargs('Collision/Shapes/b2ChainShape*')),
    apiname('b2CircleShape',
            **_api_name_kwargs('Collision/Shapes/b2CircleShape*')),
    apiname('b2EdgeShape',
            **_api_name_kwargs('Collision/Shapes/b2EdgeShape*')),
    apiname('b2PolygonShape',
            **_api_name_kwargs('Collision/Shapes/b2PolygonShape*')),
    apiname('b2BroadPhase', **_api_name_kwargs('Collision/b2BroadPhase*')),
    apiname('b2DynamicTree', **_api_name_kwargs('Collision/b2DynamicTree*')),
    apiname('b2Contact', **_api_name_kwargs('Dynamics/Contacts/b2Contact*')),
    apiname('b2ChainAndCircleContact',
            **_api_name_kwargs('Dynamics/Contacts/b2ChainAndCircleContact*')),
    apiname('b2ChainAndPolygonContact',
            **_api_name_kwargs('Dynamics/Contacts/b2ChainAndPolygonContact*')),
    apiname('b2CircleContact',
            **_api_name_kwargs('Dynamics/Contacts/b2CircleContact*')),
    apiname('b2ContactSolver',
            **_api_name_kwargs('Dynamics/Contacts/b2ContactSolver*')),
    apiname('b2EdgeAndCircleContact',
            **_api_name_kwargs('Dynamics/Contacts/b2EdgeAndCircleContact*')),
    apiname('b2EdgeAndPolygonContact',
            **_api_name_kwargs('Dynamics/Contacts/b2EdgeAndPolygonContact*')),
    apiname('b2PolygonAndCircleContact',
            **_api_name_kwargs('Dynamics/Contacts/b2PolygonAndCircleContact*')),
    apiname('b2PolygonContact',
            **_api_name_kwargs('Dynamics/Contacts/b2PolygonContact*')),
    apiname('b2Joint', **_api_name_kwargs('Dynamics/Joints/b2Joint*')),
    apiname('b2DistanceJoint',
            **_api_name_kwargs('Dynamics/Joints/b2DistanceJoint*')),
    apiname('b2FrictionJoint',
            **_api_name_kwargs('Dynamics/Joints/b2FrictionJoint*')),
    apiname('b2GearJoint', **_api_name_kwargs('Dynamics/Joints/b2GearJoint*')),
    apiname('b2MotorJoint',
            **_api_name_kwargs('Dynamics/Joints/b2MotorJoint*')),
    apiname('b2MouseJoint',
            **_api_name_kwargs('Dynamics/Joints/b2MouseJoint*')),
    apiname('b2PrismaticJoint',
            **_api_name_kwargs('Dynamics/Joints/b2PrismaticJoint*')),
    apiname('b2PulleyJoint',
            **_api_name_kwargs('Dynamics/Joints/b2PulleyJoint*')),
    apiname('b2RevoluteJoint',
            **_api_name_kwargs('Dynamics/Joints/b2RevoluteJoint*')),
    apiname('b2RopeJoint', **_api_name_kwargs('Dynamics/Joints/b2RopeJoint*')),
    apiname('b2WeldJoint', **_api_name_kwargs('Dynamics/Joints/b2WeldJoin*')),
    apiname('b2WheelJoint',
            **_api_name_kwargs('Dynamics/Joints/b2WheelJoint*')),
    apiname('b2Body', **_api_name_kwargs('Dynamics/b2Body*')),
    apiname('b2ContactManager',
            **_api_name_kwargs('Dynamics/b2ContactManager*')),
    apiname('b2Fixture', **_api_name_kwargs('Dynamics/b2Fixture*')),
    apiname('b2World', **_api_name_kwargs('Dynamics/b2World*')),
    apiname('b2DestructionListener',
            **_api_name_kwargs('Dynamics/b2WorldCallbacks*')),
    apiname('b2ContactFilter',
            **_api_name_kwargs('Dynamics/b2WorldCallbacks*')),
    apiname('b2ContactListener',
            **_api_name_kwargs('Dynamics/b2WorldCallbacks*')),
    apiname('b2QueryCallback',
            **_api_name_kwargs('Dynamics/b2WorldCallbacks*')),
    apiname('b2RayCastCallback',
            **_api_name_kwargs('Dynamics/b2WorldCallbacks*')),
    apiname('b2Rope', **_api_name_kwargs('Rope/b2Rope*')),
]

del _from_src_dir
del _api_name_kwargs
del join
del apiname
