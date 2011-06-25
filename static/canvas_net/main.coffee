x_offset = 10
y_offset = 10
nodes = []

class Node
  constructor: (@x, @y) ->
    @connections = []
  
  draw: (ctx) ->
    ctx.strokeRect @x, @y, 10, 10
    for connection in @connections
      ctx.beginPath()
      ctx.moveTo(@x, @y)
      ctx.lineTo(connection.x, connection.y)
      ctx.stroke()

draw = (ctx) ->
  for node in nodes
    node.draw(ctx)
  
initialize_nodes = ->
  for i in [0...10]
    this_x = Math.random() * 800
    this_y = Math.random() * 500
      
    nodes.push(new Node(this_x, this_y))
  
  for node in nodes
    for i in [0..5]
      node.connections.push nodes[Math.floor(Math.random() * nodes.length)]

initialize_canvas = ->
  canvas = $("canvas").get(0)
  ctx = canvas.getContext "2d"
  
  setInterval(->
    draw ctx
  , 10)


$( ->
  initialize_canvas()
  initialize_nodes()
)