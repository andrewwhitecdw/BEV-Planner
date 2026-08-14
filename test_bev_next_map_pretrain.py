import runpy


def test_map_pretrain_cat2id_matches_map_classes():
    config = runpy.run_path('configs/bev_next/map_pretrain.py')
    for idx, cls in enumerate(config['map_classes']):
        assert config['cat2id'][cls] == idx, (
            f'cat2id[{cls!r}] should be {idx} to match map_classes order, '
            f'got {config["cat2id"][cls]}')
