{ pkgs ? import <nixpkgs> {} }:

let
  libs = with pkgs; [
    xorg.libX11
    xorg.libXcursor
    xorg.libXrandr
    xorg.libXi
    xorg.libXinerama
    wayland
    libxkbcommon
    stdenv.cc.cc.lib
  ];
in

pkgs.mkShell {
  buildInputs = [ pkgs.python3 ];

  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath libs;
}
