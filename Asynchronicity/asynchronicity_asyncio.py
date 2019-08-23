import asyncio

async def square(x):
    print(f'Starting square with arg {x}!')
    await asyncio.sleep(5)
    print(f'Finishing square with arg {x}!')
    return x * x 

async def cube(x):
    print(f'Starting cube with arg {x}!')
    await asyncio.sleep(5)
    y = await square(x)
    print(f'Finishing cube with arg {x}!')
    return y * x

loop = asyncio.get_event_loop()
coro = asyncio.gather(cube(1), cube(2), cube(3))
result = loop.run_until_complete(coro)
# Starting cube with arg 1!
# Starting cube with arg 2!
# Starting cube with arg 3!
# Starting square with arg 1!
# Starting square with arg 2!
# Starting square with arg 3!
# Finishing square with arg 1!
# Finishing cube with arg 1!
# Finishing square with arg 2!
# Finishing cube with arg 2!
# Finishing square with arg 3!
# Finishing cube with arg 3!