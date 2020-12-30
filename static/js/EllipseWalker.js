
module.exports = class EllipseWalker{
  constructor(x,y,dx,dy, test){
    this.x  =  x;
    this.y  =  y;
    this.dx = dx/2;
    this.dy = dy/2;
    // if (test==true){
    //   stroke(100)
    //   ellipse(x,y,dx,dy)
    // }
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
    var x_bounds = this.getXBounds()
    var interval = (x_bounds[1]-x_bounds[0])/n
    console.log(interval)
    var xValues = [];
    for(var i =0; i<=n;i++){
      console.log(interval*i)
      xValues.push(x_bounds[0]+interval*i)
    }
    return xValues
  }

  getXBounds(){
    return [this.x-this.dx/2, this.x+this.dx/2]
  }
}
