var canvasX = 400;
var canvasY = 400;
var testList = ["A1","A2","A3"];
var a1_childs = ["B1","B1", "B1", "B1"]
var a2_childs = ["B2","B2", "B2", "B3"]
var a3_childs = ["B3", "B3", "B3", "B3"]
var xLim = canvasX/3*4;
var yLim = canvasY/4*4;

function setup() {
  createCanvas(canvasX, canvasY);
  background(80)
  textAlign(CENTER)
  ell = new EllipseWalker(canvasX/2+40, canvasY/2+40,canvasX/3,canvasY/4,true)
}

function draw() {
  // for (var i = 0; i<xLim;i++){
  //   point(i,ellipse.walkX(-i))
  //   point(i,ellipse.walkX(i))
  // }

  // stroke(255,0,255);
  // for (var i = 100; i<yLim;i=i+5){
  //   point(ell.walkY(i),i)
  //   point(ell.walkY(-i),i)
  // }
  console.log(ell.walkNX(20))
  // defining first quadrant
  // Node1 = new WordNode('A1',2*canvasX/3+(canvasX/8)/2, canvasY/3, 'A', a1_childs)
  // ellipse(2*canvasX/3+(canvasX/8)/2,canvasY/3,canvasX/3,canvasY/3);
  // // defining second quadrant
  // ellipse(canvasX/3-(canvasX/8)/2,canvasY/3,canvasX/3,canvasY/3);
  // Node2 = new WordNode('A2',canvasX/3-(canvasX/8)/2,canvasY/3,'A',a2_childs);
  //
  // // defining third quadrant
  // ellipse(canvasX/2,canvasY/3*2,canvasX/3,canvasY/3);
  // Node3 = new WordNode('A3',canvasX/2,canvasY/3*2,'A', a3_childs);
  // stroke(255);
  // point(canvasX, p1);
  // point(p1, p3);
  // point(p2, p4);
  // point(p3, p1);
  // point(p4, p2);
  // point(p4, p4);
}

class EllipseWalker{
  constructor(x,y,dx,dy, test){
    this.x  =  x;
    this.y  =  y;
    this.dx = dx/2;
    this.dy = dy/2;
    if (test==true){
      stroke(100)
      ellipse(x,y,dx,dy)
    }
  }

  walkY(y){
    var yScale = (Math.pow(Math.abs(y)-this.y,2)/Math.pow(this.dy,2));
    var xDim   = Math.pow(this.dx,2)
    var term   = xDim*(1-yScale)
    if (y<0){
      return -Math.sqrt(term)+this.x
    }
    return Math.sqrt(term)+this.x
  }

  walkX(x){
    var xScale = (Math.pow(Math.abs(x)-this.x,2)/Math.pow(this.dx,2))
    var yDim = Math.pow(this.dy,2)
    var term = yDim*(1 - xScale)
    if (x<0){
      return -Math.sqrt(term)+this.x
    }
    return Math.sqrt(term) +this.y
  }

  walkNX(n){
    x_bounds = getXBounds()
    interval = x_bounds[1]-x_bounds[0]
    var xValues = [];
    for(var i =0; i++;n){
      xValues.push(x_bounds[0]+interval*i)
    }
    return xValuess
  }
  getXBounds(){
    return [this.x-this.dx/2, this.x+this.dx/2]
  }
}

function getSize(s){
  if (s=='A'){
    return [canvasX*(1/8),canvasY*(1/12)];
  }
  if (s=='B'){
    return [canvasX*(1/10),canvasY*(1/12)];
  }
}



class WordNode{
  constructor(id,x,y,s,childList){
    this.id = id
    this.x = x
    this.y = y
    var ellipse_size = getSize(s)
    fill(255)
    text(this.id, x, y);
    this.childs = childList
    noFill()
    ellipse(this.x,this.y,ellipse_size[0],ellipse_size[1]);
    this.constructChilds()
  }

  constructChilds(){
    console.log("Displayed childs")
    var numberOfChilds = this.childs.length
    console.log(numberOfChilds)
  }
}
