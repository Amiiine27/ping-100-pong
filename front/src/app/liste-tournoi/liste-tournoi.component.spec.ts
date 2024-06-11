import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListeTournoiComponent } from './liste-tournoi.component';

describe('ListeTournoiComponent', () => {
  let component: ListeTournoiComponent;
  let fixture: ComponentFixture<ListeTournoiComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ListeTournoiComponent]
    });
    fixture = TestBed.createComponent(ListeTournoiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
