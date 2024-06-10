import { TestBed } from '@angular/core/testing';

import { AjoutTournoiService } from './ajout-tournoi.service';

describe('AjoutTournoiService', () => {
  let service: AjoutTournoiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AjoutTournoiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
