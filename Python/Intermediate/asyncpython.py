import asyncio,time

async def brew_coffee():
    print("Started Brewing coffee")
    await asyncio.sleep(3)
    print("End brewing Coffee")
    return "Coffee ready"


async def toastBagel():
    print("Started toasting Bagel")
    await asyncio.sleep(2)
    print("End toasting bagel")
    return "bagel ready"

async def main():
    starttime = time.time()
    
    #batch = asyncio.gather(brew_coffee(),toastBagel()) #this is batch method
    #result_coffee,result_bagel = await batch

    coffee_task = asyncio.create_task(brew_coffee()) #this lternate method using asyncio.create_task
    bagel_task = asyncio.create_task(toastBagel())
    result_coffee = await coffee_task
    result_bagel = await bagel_task

    endtime = time.time()
    elapsed_time = endtime - starttime
    print(f'result of brew coffee : {result_coffee}')
    print(f'result of toasting bagel : {result_bagel}')
    print(f'Total time taken for the task is {elapsed_time} seconds')

if __name__ == '__main__':
    asyncio.run(main())