
module.exports = class WordNode{
  static this.arr = [];
  constructor(id,x,y,s,childList){
    this.id = id
    this.x = x
    this.y = y
    arr
    var ellipse_size = getSize(s)
    // fill(255)
    // text(this.id, x, y);
    this.childs = childList
    // noFill()
    // ellipse(this.x,this.y,ellipse_size[0],ellipse_size[1]);
    this.constructChilds()
  }

  constructChilds(){
    // in order to construct the childs, we have to know how they relate to each other
    console.log("Displayed childs")
    var numberOfChilds = this.childs.length
    console.log(numberOfChilds)
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
