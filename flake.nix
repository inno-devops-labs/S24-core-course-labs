{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfreePredicate = pkg: builtins.elem pkg.pname [
            "vault"
          ];
        };
      in with pkgs; {
        devShells.default = mkShell {
          packages = [
            kubernetes
            minikube
            (wrapHelm kubernetes-helm {
              plugins = with kubernetes-helmPlugins; [
                helm-secrets
              ];
            })

            sops
          ];
        };
      }
    );
}
