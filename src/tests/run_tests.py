import asyncio

# Define test cases
test_cases = {
    "get_user": lambda: __import__("get_user_id").test(),
    "get_user_by_username": lambda: __import__("get_user_username").test(),
    "get_leaderboard_global": lambda: __import__("get_leaderboard_global").test(),
    "get_leaderboard_country": lambda: __import__("get_leaderboard_country").test(),
    "get_leaderboard_score": lambda: __import__("get_leaderboard_score").test(),
    "get_leaderboard_score_country": lambda: __import__("get_leaderboard_score_country").test(),
}

success = 0
failed = 0

async def main():
    global success, failed
    print(f"Running {len(test_cases)} tests...\n")
    
    for name, func in test_cases.items():
        print(f"Running test '{name}'...")
        try:
            await func()
            print(f"✅ Test '{name}' ran successfully\n")
            success += 1
        except Exception as err:
            print(f"❌ Error in test '{name}': {err}\n")
            failed += 1

    print("=== Test Summary ===")
    print(f"✅ Tests successful: {success}")
    print(f"❌ Tests failed: {failed}")
    print(f"🧪 Total tests run: {success + failed}")

if __name__ == "__main__":
    asyncio.run(main())
