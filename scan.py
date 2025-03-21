import asyncio
from switchbot import GetSwitchbotDevices

async def main():
    discovery = GetSwitchbotDevices()
    while True:
        devices = await discovery.discover(scan_timeout=2)
        for address, adv_data in devices.items():
            if adv_data.data['data']:
                print(f"Address: {address}")
                print(f"  Name: {adv_data.data['modelFriendlyName']}")
                print(f"  Data: {adv_data.data['data']}")
                print(f"  RSSI: {adv_data.rssi}")
                print("-" * 20)

if __name__ == "__main__":
    asyncio.run(main())

