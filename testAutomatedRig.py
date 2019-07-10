import maya.cmds as cmds
import maya.mel as mel
import sys

sc = 0
locs = cmds.ls ('*_LOC')

for loc in locs:
	parLoc = cmds.listRelatives(loc, p = 1)

	#joints positioning
	cmds.select(cl = 1)
	jnt = cmds.joint(n = loc.replace('_LOC', '_JNT'), sc = sc)
	const = cmds.parentConstraint(loc, jnt)
	cmds.delete(const)
	cmds.makeIdentity(jnt, a = 1, t = 1, r = 1, s = 1)

	if parLoc:
		parJnt = parLoc[0].replace ('_LOC', '_JNT')
		cmds.parent(jnt, parJnt)

	# controls curves creation and positioning
	control = cmds.circle(n = loc.replace('_LOC', '_CTRL'), ch = 0)
	grp = cmds.group(n = loc.replace('_LOC', '_GRP'), em = 1, w = 1)
	cmds.parent(control, grp)
	const = cmds.parentConstraint(loc, control)
	cmds.delete(const)
	cmds.parentConstraint(control, jnt)
	if parLoc:
		parCont = parLoc[0].replace('_LOC', '_CTRL')
		cmds.parent(grp, parCont)

cmds.delete(locs)