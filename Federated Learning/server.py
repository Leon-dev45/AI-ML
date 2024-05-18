import flwr as fl

def weighted_average(metrics):
    accuracies = [num_examples * m['accuracy'] for num_examples, m in metrics]
    print(accuracies)
    examples = [num_examples for num_examples, _ in metrics]
    print(examples)
    return {"accuracy": sum(accuracies) / sum(examples)}

fl.server.start_server(
    server_address="SERVER_ADDRESS",
    config=fl.server.ServerConfig(num_rounds=3),
    strategy=fl.server.strategy.FedAvg(
        evaluate_metrics_aggregation_fn=weighted_average,
    )
)