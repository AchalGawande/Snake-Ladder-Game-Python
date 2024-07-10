from userInterface import *
import cProfile
import pstats

def main():
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("850x600")
    img = PhotoImage(file="lenna.gif")
    x = Display(master, img)
    master.mainloop()

if __name__ == "__main__":
    # Profile the main function
    profiler = cProfile.Profile()
    profiler.enable()
    
    main()
    
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()

    # Optionally, you can save the profiling results to a file
    stats.dump_stats("snake_and_ladder_profiler_results.prof")
