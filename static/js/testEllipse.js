var path = require('path');
var EllipseWalker = require( path.resolve( __dirname, "static/js/EllipseWalker.js" ) );
var WordNode = require( path.resolve( __dirname, "static/js/WordNode.js" ) );
canvasX = 400;
canvasY = 400;

var testList = ["A1","A2","A3"];
var a1_childs = ["B1","B1", "B1", "B1"]
var a2_childs = ["B2","B2", "B2", "B3"]
var a3_childs = ["B3", "B3", "B3", "B3"]
var xLim = canvasX/3*4;
var yLim = canvasY/4*4;

ellipse =new EllipseWalker(canvasX/2, canvasY/2,canvasX/4,canvasY/4,true);
var interval_points = ellipse.walkNX(10);
interval_points

Node1 = new WordNode('A1',2*canvasX/3+(canvasX/8)/2, canvasY/3, 'A', a1_childs)
// defining second quadrant
Node2 = new WordNode('A2',canvasX/3-(canvasX/8)/2,canvasY/3,'A',a2_childs);

// defining third quadrant
Node3 = new WordNode('A3',canvasX/2,canvasY/3*2,'A', a3_childs);
