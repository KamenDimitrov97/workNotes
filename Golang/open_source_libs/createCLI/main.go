package main

import (
	"fmt"

	"github.com/spf13/cobra"
)

func main() {
	rootCmd := &cobra.Command{
		Use:   "mycli",
		Short: "MyCLI is a simple CLI tool",
		Long:  "A simple CLI tool to demonstrate Cobra",
		Run: func(cmd *cobra.Command, args []string) {
			// This will run if no subcommands are specified
			fmt.Println("Hello from MyCLI!")
		},
	}

	rootCmd.AddCommand(greetCmd)
	rootCmd.Execute()
}

var greetCmd = &cobra.Command{
	Use:   "greet [name]",
	Short: "Greet the user",
	Long:  `This command greets the user with the provided name.`,
	Args:  cobra.MinimumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		name := args[0]
		fmt.Printf("Hello, %s!\n", name)
	},
}
