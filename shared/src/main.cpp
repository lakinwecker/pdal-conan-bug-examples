#include <pdal/StageFactory.hpp>
#include <pdal/PluginManager.hpp>

#include <iostream>

int main() {
    std::cout << "Printing available plugins!" << std::endl;
    for (auto const &name : pdal::PluginManager<pdal::Stage>::names()) {
        std::cout << "Available Plugin: " << name << std::endl;
    }
    std::cout << "Done!" << std::endl;
}
