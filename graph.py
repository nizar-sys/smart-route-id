def load_graph():
    return {
        "jakarta": {
            "bogor": {"jarak": 57},
            "depok": {"jarak": 27},
            "tangerang": {"jarak": 34},
            "bekasi": {"jarak": 24}
        },
        "bogor": {
            "jakarta": {"jarak": 57},
            "depok": {"jarak": 46},
            "tangerang": {"jarak": 74},
            "bekasi": {"jarak": 56}
        },
        "depok": {
            "jakarta": {"jarak": 27},
            "bogor": {"jarak": 46},
            "tangerang": {"jarak": 40},
            "bekasi": {"jarak": 42}
        },
        "tangerang": {
            "jakarta": {"jarak": 34},
            "bogor": {"jarak": 74},
            "depok": {"jarak": 40},
            "bekasi": {"jarak": 65}
        },
        "bekasi": {
            "jakarta": {"jarak": 24},
            "bogor": {"jarak": 56},
            "depok": {"jarak": 42},
            "tangerang": {"jarak": 65}
        }
    }
