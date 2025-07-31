from marshal import version

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDolfinxMpc(PythonPackage):
    """Python interface of DOLFINx-MPC, an extension of DOLFINx for multipoint constraints."""

    homepage = "https://www.jsdokken.com/dolfinx_mpc"
    url = "https://github.com/jorgensd/dolfinx_mpc/archive/v0.9.3.tar.gz"

    maintainers("jorgensd")

    license("MIT", checked_by="jorgensd")

    version("0.9.3", sha256="efa312cc498e428aab44acccc9bb0c74c200eda005742de7778c8e68fa84e8df")
    version("0.9.2", sha256="8681def964aef0101b7e35aa377cfbcc4b220a20cfc540ec9058b324031b58c2")
    version("0.9.1", sha256="2d0c3583b8d69ad4374b0938cd157c9ca48acf50d6969e51ccce8ab14625040e")
    version("0.9.0", sha256="9b87cd75e3b26b3f92b600e935c45677624c8e169782bf6646265d1e03a0e043")
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.21:", when="@0.9:", type="build")

    depends_on("py-packaging")

    depends_on("python@3.9:", when="@0.9:", type=("build", "run"))

    depends_on("dolfinx-mpc@main", when="@main")
    depends_on("dolfinx-mpc@0.9.3", when="@0.9.3")
    depends_on("dolfinx-mpc@0.9.2", when="@0.9.2")
    depends_on("dolfinx-mpc@0.9.1", when="@0.9.1")
    depends_on("dolfinx-mpc@0.9.0", when="@0.9.0")

    depends_on("py-fenics-dolfinx@main", when="@main")
    depends_on("py-fenics-dolfinx@0.9", when="@0.9")

    depends_on("py-nanobind@2:", when="@0.9:", type="build")
    depends_on("py-scikit-build-core+pyproject@0.10:", when="@0.10:", type="build")
    depends_on("py-scikit-build-core+pyproject@0.5:", when="@0.8:0.9", type="build")

    depends_on("py-petsc4py", type=("build", "run"))

    variant("numba", default=False, description="numba support")
    depends_on("py-numba", when="+numba", type=("run"))

    build_directory = "python"
